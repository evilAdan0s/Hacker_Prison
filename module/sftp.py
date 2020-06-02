#!/usr/bin/env python

# SFTP模块 用来上传或下载文件

import paramiko

class Sftp:
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
	def sftpLoginPassword(self):
		transport = paramiko.Transport((self.host, self.port))
		transport.connect(username=self.username,password=self.password)
		sftp = paramiko.SFTPClient.from_transport(transport)
		self.__sftp = sftp
		self.__transport = transport

	# 密钥登录
	def sftpLoginSecretKey(self):
		private_key = paramiko.RSAKey.from_private_key_file(self.key)
		transport = paramiko.Transport((self.host, self.port))
		transport.connect(username=self.username, pkey=private_key )
		sftp = paramiko.SFTPClient.from_transport(transport)
		self.__sftp = sftp
		self.__transport = transport

	def sftpMain(self):
		if self.flag == 1:
			sftpLoginPassword(self)
		elif self.flag == 2:
			sftpLoginSecretKey(self)
		else:
			print("\033[0;31m%s\033[0m" % ("[!] Something Wrong!"))

	# 上传功能
	def sftpUpload(self, local_path, target_path):
		self.__sftp.put(local_path, target_path)

	# 下载功能
	def sftpDownload(self, target_path, local_path):
		self.__sftp.get(self, target_path, local_path)

	# 关闭连接
	def closeSftp(self):
		self.__transport.close()

