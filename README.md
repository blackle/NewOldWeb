# extremely simple python+htmx+lighttpd project

To use, change `server.document-root` in `lighttpd.conf` to the absolute path to "public" and run:

```
lighttpd -D -f ./lighttpd.conf
```