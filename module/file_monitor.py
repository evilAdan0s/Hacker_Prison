#!/usr/bin/env python

# 文件监控模块

import ssh_login, time, re

class FileMonitor:

	local_file = './fileLog.txt'

	def getFileList(self, dir, loginList, loginFlag):
		if loginFlag == 1:
			ssh = ssh_login.SshLogin(loginList['host'], loginList['port'], loginList['username'], loginList['password'])
			ssh.sshLoginPassword()
			ssh.execute("ls -aln %s | stat `awk'{print $9}'` | grep -v Size | grep -v Birth | grep -v Device | grep -v Access | grep -v Change" % dir)
			#fileWrite(ssh.__result)
			self.__fileResult = ssh.__result
			ssh.sshClose()
		elif loginFlag == 2:
			ssh = ssh_login.SshLogin(loginList['host'], loginList['port'], loginList['username'], loginList['key'])
			ssh.sshLoginPassword()
			ssh.execute("ls -aln %s | stat `awk'{print $9}'` | grep -v Size | grep -v Birth | grep -v Device | grep -v Access | grep -v Change" % dir)
			#fileWrite(ssh.__result)
			self.__fileResult = (str(ssh.__result)).split("\n") # 即时的文件名
			ssh.sshClose()
		else:
			print("\033[0;31m%s\033[0m" % ("[!] Something Wrong!"))
	def fileWrite(self, fileContent):
		f = open(self.local_file, 'w')
		f.write(fileContent)
		f.close()

	def fileRead(self):
		f = open(self.local_file, 'r')
		fileContentList = f.readlines()
		self.__fileContentList = fileContentList #文件里的文件名

	def fileProcess(self):
		self.fileRead()
		if (self.__fileResult == self.__fileContentList) is True: #之前的文件名和修改时间与即时无差异
			print("\033[0;32m%s\033[0m" % ("[*] " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "文件无异常"))
		elif len(self.__fileResult) != len(self.__fileContentList): #文件数有差异
			fileResultStr = "".join(self.__fileResult)
			fileContentListStr = "".join(self.__fileContentList)
			p = re.compile(r"\'(.*)\'")
			fileList1 = p.findall(fileResultStr)
			fileList2 = p.findall(fileContentListStr)
			
			for i in fileList1:
				if i not in fileList2:
					print("\033[0;31m%s\033[0m" % ("[!] 有新增文件：" + i))
			for i in fileList2:
				if i not in fileList1:
					print("\033[0;31m%s\033[0m" % ("[!] 有被删除文件：" + i))


		elif (self.__fileResult == self.__fileContentList) is False: #时间有差异
			print("\033[0;31m%s\033[0m" % ("[!] 近期有文件被修改！"))












