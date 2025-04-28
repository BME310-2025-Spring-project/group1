import os
import paramiko
import boto3
from pathlib import Path

def deploy():
    # Server details from environment variables
    server_host = os.environ.get('SERVER_HOST')
    ssh_key_path = 'ssh_key'
    app_path = '/home/ubuntu/app'

    # SSH client setup
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_host, username='ubuntu', key_filename=ssh_key_path)

    # SCP files to server
    sftp = ssh.open_sftp()
    for file in Path('build').glob('*'):
        sftp.put(str(file), f'{app_path}/{file.name}')
    sftp.close()

    # Install dependencies and restart service
    commands = [
        f'cd {app_path} && python3 -m pip install -r requirements.txt',
        'sudo systemctl restart myapp.service'
    ]
    for cmd in commands:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
        if stderr.read():
            print(f'Error: {stderr.read().decode()}')

    ssh.close()

if __name__ == '__main__':
    deploy()