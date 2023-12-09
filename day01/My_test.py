import pyperclip
from flask import Flask

app = Flask(__name__)
paste_text = '用友'
data_path = 'D:\工作\yonyouTK.txt'
f = open(data_path, encoding='utf-8')
all_lines = f.readlines()


# print(all_lines)

@app.route('/answer')
def answer():
    script = "<script>setTimeout(function(){window.location.reload();},3000);</script>"
    paste_text = pyperclip.paste()
    if not paste_text:
        lines = all_lines[0:10]
    else:
        lines = []
        for l in all_lines:
            if l.find(paste_text) >= 0:
                lines.append(l)
            if len(lines) > 10:
                break
    return script + "<br/><br/>".join(lines)


if __name__ == '__main__':
    app.run(debug=False, threaded=True, port=16888, host='0.0.0.0')
