#!/usr/bin/env python

# ssh登录模块

import paramiko

class SshLogin:
	host = ''
	port = 22
	username = ''
	password = ''
	key = ''
	flag = 1

	def __init__(self, host, port, username, password = '', key = '', flag = 1):
		self.host = host
		self.port = port
		self.username = username
		self.password = password
		self.key = key
		self.flag = flag

	# 密码登录
	def sshLoginPassword(self):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
		self.__ssh = ssh

	# 密钥登录
	def sshLoginSecretKey(self):
		private_key = paramiko.RSAKey.from_private_key_file(self.key)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=self.host, port=self.port, username=self.username, key=private_key)
		self.__ssh = ssh

	def loginMain(self):
		if self.flag == 1:
			sshLoginPassword(self)
		elif self.flag == 2:
			sshLoginSecretKey(self)
		else:
			print("\033[0;31m%s\033[0m" % ("[!] Something Wrong!"))


	# 执行命令
	def execute(self, command):
		stdin, stdout, stderr = self.__ssh.exec_command(command)
		result = stdout.read()
		self.__result = result

	# 关闭连接 
	def sshClose(self):
		self.__ssh.close()


	





