# 设置本镜像需要使用的基础镜像
FROM openjdk:8

LABEL key="Joword"

# 把 app.jar 包添加到镜像中
ADD test.jar /app.jar

# 镜像暴露的端口
EXPOSE 9568

RUN bash -c 'touch /app.jar'

# 容器启动命令
ENTRYPOINT ["java","-jar","/app.jar"]

# 设置时区
RUN /bin/cp /usr/share/zoneinfo/Asia/Guangdong /etc/localtime && echo 'Asia/Guangdong' >/etc/timezone
