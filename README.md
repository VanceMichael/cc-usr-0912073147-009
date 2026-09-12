# 驾培合同退费服务

后端接收合同编号和已消费信息，当前入口返回核算排队状态，为费率版本、时区处理和复核留出边界。金额快照应在后续 SQLite 层实现。

```bash
pytest
docker build -t refund-service .
docker run --rm -p 8000:8000 refund-service
```

