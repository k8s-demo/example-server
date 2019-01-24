#!/usr/bin/env python3
import pathlib
import socket
import subprocess

import flask

app = flask.Flask(__name__)
hostname = socket.gethostname()
accessed_times_file = pathlib.Path("/mnt/viewcounter.txt")

@app.route("/")
def example():
	if not accessed_times_file.exists():
		accessed_times_file.write_text("0")
	accessed_times = int(accessed_times_file.read_text())
	accessed_times += 1
	accessed_times_file.write_text(str(accessed_times))
	return "Hello<br/>I am running on pod %s.<br/>This page has been accessed %d times.\n" % (hostname, accessed_times)

@app.route("/slow/")
def slow():
	return subprocess.check_output(["openssl", "dhparam", "-out", "/dev/null", "2048"], stderr=subprocess.STDOUT)

if __name__ == "__main__":
	app.run(host="0.0.0.0")
