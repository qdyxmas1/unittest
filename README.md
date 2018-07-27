# unittest
# unittest
https://oapi.dingtalk.com/robot/send?access_token=9abd2d571e04062a758732ec2b37b2c01e69b4249e24a37a68a76916028c4759
# 自动化部署 #

## 	下载安装utx和coverage ##
	git clone https://github.com/qdyxmas/utx.git
	cd utx
	python3 setup.py install
	pip3 install coverage
	pip3 install colorama
	拷贝testrun.py到后台的根目录下
## github webhooks ##
	在需要自动部署的项目上面添加hooks,保证每次push都能自动触发
	单元测试和环境部署
	测试主机收到hooks后触发更新该项目代码,然后调用单元测试
## 搭建WEB服务器 ##
	每次运行后端日照存放到WEB服务器上
	
	
Testing....
	