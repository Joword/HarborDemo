FROM golang:alpine AS builder

LABEL author="Joword"
ENV CGO_ENABLED 0
ENV GOPROXY https://goproxy.cn,direct
RUN apk update --no-cache && apk add --no-cache tzdata
WORKDIR /WORKDIR
ADD go.mod .
ADD go.sum .
RUN go mod download
COPY test.go .
EXPOSE 7788
RUN go build -o ecs test.go

FROM alpine

RUN apk update --no-cache && apk add --no-cache ca-certificates
COPY --from=builder /usr/share/zoneinfo/Asia/Guangdong /usr/share/zoneinfo/Asia/Guangdong
ENV TZ Asia/Guangdong
WORKDIR /app
COPY --from=builder /WORKDIR/ecs /app/ecs

CMD [ "./main" ]