#!/usr/bin/env python
import ssh_login

class HostVul:

	def kernelAbout(self, loginList):
		ssh = ssh_login.SshLogin(loginList['host'], loginList['port'], loginList['username'], loginList['password'], loginList['key'],loginList['flag'])
		ssh.loginMain()
		sh.execute("echo -e '\n内核相关:' && uname -a && cat /etc/*-release && echo -e '\n计划任务:' && cat /etc/crontab")
		print(ssh.__result)
		ssh.sshClose()

	def portAbout(self, loginList):
		ssh = ssh_login.SshLogin(loginList['host'], loginList['port'], loginList['username'], loginList['password'], loginList['key'],loginList['flag'])
		ssh.loginMain()
		sh.execute("echo -e '\n开放端口:' &&  netstat -antupl")
		print(ssh.__result)
		ssh.sshClose()

	def vulAbout(self):
		print("[*] 漏洞建议模块正在开发中......")