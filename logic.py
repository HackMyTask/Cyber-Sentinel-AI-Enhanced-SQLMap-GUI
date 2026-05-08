"""
SQLMap Wrapper Logic
Handles subprocess management and command execution
"""

import subprocess
import threading
import queue
import os
from typing import Callable, Optional, List


class SQLMapWrapper:
    """Manages SQLMap execution and output streaming"""
    
    def __init__(self, output_callback: Callable[[str], None]):
        """
        Initialize SQLMap Wrapper
        
        Args:
            output_callback: Function to call with each line of output
        """
        self.output_callback = output_callback
        self.process: Optional[subprocess.Popen] = None
        self.is_running = False
        self.output_queue = queue.Queue()
        self.full_output = []
        
    def build_command(self, 
                     target_url: str,
                     risk: int = 1,
                     level: int = 1,
                     random_agent: bool = False,
                     batch: bool = True,
                     tamper: str = 'None',
                     proxy: str = '',
                     additional_args: str = '') -> List[str]:
        """
        Build SQLMap command from parameters
        
        Args:
            target_url: Target URL to scan (or file path for multiple targets)
            risk: Risk level (1-3)
            level: Level (1-5)
            random_agent: Use random user agent
            batch: Never ask for user input
            tamper: Tamper script to use
            proxy: Proxy to use (or file path for multiple proxies)
            additional_args: Additional command line arguments
            
        Returns:
            Command as list of strings
        """
        # Check if sqlmap is available
        sqlmap_cmd = self._find_sqlmap()
        
        # Check if target_url is a file (multiple targets)
        if target_url.endswith('.txt'):
            cmd = [sqlmap_cmd, '-m', target_url]
        else:
            cmd = [sqlmap_cmd, '-u', target_url]
        
        # Add risk and level
        cmd.extend(['--risk', str(risk)])
        cmd.extend(['--level', str(level)])
        
        # Add flags
        if random_agent:
            cmd.append('--random-agent')
        
        if batch:
            cmd.append('--batch')
        
        # Add tamper script
        if tamper and tamper != 'None':
            cmd.extend(['--tamper', tamper])
        
        # Add proxy
        if proxy:
            if proxy.endswith('.txt'):
                # Multiple proxies from file
                cmd.extend(['--proxy-file', proxy])
            else:
                # Single proxy
                cmd.extend(['--proxy', proxy])
        
        # Add additional arguments
        if additional_args:
            cmd.extend(additional_args.split())
        
        return cmd
    
    def _find_sqlmap(self) -> str:
        """
        Find SQLMap executable
        
        Returns:
            Path to sqlmap or 'sqlmap' if in PATH
        """
        # Try common locations
        common_paths = [
            'sqlmap',
            'sqlmap.py',
            'python -m sqlmap',
            os.path.expanduser('~/sqlmap/sqlmap.py'),
            'C:\\sqlmap\\sqlmap.py',
        ]
        
        # For now, return 'sqlmap' and assume it's in PATH
        # Users can modify this based on their installation
        return 'sqlmap'
    
    def start_scan(self, command: List[str]):
        """
        Start SQLMap scan in a separate thread
        
        Args:
            command: Command to execute
        """
        if self.is_running:
            self.output_callback("⚠️ Scan already running!\n")
            return
        
        self.is_running = True
        self.full_output = []
        
        # Start scan in separate thread
        scan_thread = threading.Thread(target=self._run_scan, args=(command,))
        scan_thread.daemon = True
        scan_thread.start()
    
    def _run_scan(self, command: List[str]):
        """
        Execute SQLMap command and stream output
        
        Args:
            command: Command to execute
        """
        try:
            self.output_callback(f"🚀 Executing: {' '.join(command)}\n")
            self.output_callback("=" * 80 + "\n")
            
            # Start process with PIPE for stdout and stderr
            self.process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                stdin=subprocess.PIPE,
                universal_newlines=True,
                bufsize=1,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            
            # Read output line by line
            for line in iter(self.process.stdout.readline, ''):
                if line:
                    self.full_output.append(line)
                    self.output_callback(line)
            
            # Wait for process to complete
            self.process.wait()
            
            # Check return code
            if self.process.returncode == 0:
                self.output_callback("\n✅ Scan completed successfully!\n")
            else:
                self.output_callback(f"\n⚠️ Scan finished with code: {self.process.returncode}\n")
        
        except FileNotFoundError:
            self.output_callback("\n❌ ERROR: SQLMap not found!\n")
            self.output_callback("Please ensure SQLMap is installed and in your PATH.\n")
            self.output_callback("Install: pip install sqlmap\n")
            self.output_callback("Or download from: https://github.com/sqlmapproject/sqlmap\n")
        
        except Exception as e:
            self.output_callback(f"\n❌ ERROR: {str(e)}\n")
        
        finally:
            self.is_running = False
            self.process = None
    
    def stop_scan(self):
        """Stop the running scan"""
        if self.process and self.is_running:
            try:
                self.process.terminate()
                self.output_callback("\n🛑 Scan stopped by user\n")
            except Exception as e:
                self.output_callback(f"\n❌ Error stopping scan: {str(e)}\n")
            finally:
                self.is_running = False
                self.process = None
        else:
            self.output_callback("⚠️ No scan is currently running\n")
    
    def get_recent_output(self, lines: int = 20) -> str:
        """
        Get recent output lines for AI analysis
        
        Args:
            lines: Number of recent lines to return
            
        Returns:
            Recent output as string
        """
        if not self.full_output:
            return ""
        
        recent = self.full_output[-lines:]
        return ''.join(recent)
    
    def get_full_output(self) -> str:
        """
        Get full output
        
        Returns:
            Full output as string
        """
        return ''.join(self.full_output)
