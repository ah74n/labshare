import os
from flask import Flask, request, render_template_string, send_from_directory, redirect, url_for

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'shared_files')

# Create the shared folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Monochromatic Dark UI inspired by modern Framer templates
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LABSHARE// LOCAL FILE LAYER</title>
    <style>
        :root {
            --bg: #0a0a0a;
            --card-bg: #121212;
            --border: #265626;
            --border-focus: #ffffff;
            --text-primary: #ffffff;
            --text-secondary: #a3a9a3;
            --text-muted: #527252;
            --accent: #ffffff;
            --danger: #ef4444;
            --success: #22c55e;
            --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg); 
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px 20px;
            letter-spacing: -0.02em;
        }

        .container { 
            background: var(--card-bg); 
            padding: 48px; 
            border-radius: 0px; 
            border: 1px solid var(--border);
            width: 100%;
            max-width: 600px; 
        }

        header {
            margin-bottom: 40px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 24px;
        }

        .badge {
            font-family: var(--font-mono);
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--text-secondary);
            border: 1px solid var(--border);
            padding: 4px 8px;
            display: inline-block;
            margin-bottom: 16px;
        }

        h1 { 
            font-size: 36px;
            font-weight: 800;
            letter-spacing: -0.04em;
            text-transform: uppercase;
            line-height: 1;
            margin-bottom: 8px;
        }

        .subtitle {
            font-size: 14px;
            color: var(--text-secondary);
            font-weight: 400;
        }

        .dropzone {
            border: 1px dashed var(--border);
            padding: 32px;
            text-align: center;
            background: #171717;
            cursor: pointer;
            margin-bottom: 20px;
            transition: border-color 0.2s ease, background 0.2s ease;
        }

        .dropzone:hover {
            border-color: var(--border-focus);
            background: #1c1c1c;
        }

        .dropzone input[type="file"] {
            display: none;
        }

        .file-label {
            font-weight: 600;
            color: var(--text-primary);
            font-size: 15px;
            text-transform: uppercase;
            font-family: var(--font-mono);
            letter-spacing: 0.05em;
        }

        .file-chosen-name {
            font-size: 13px;
            color: var(--text-secondary);
            margin-top: 8px;
            font-family: var(--font-mono);
            word-break: break-all;
        }

        .btn-submit { 
            background: var(--accent); 
            color: #000000; 
            border: 1px solid var(--accent); 
            padding: 16px; 
            cursor: pointer; 
            font-size: 14px; 
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-family: var(--font-mono);
            width: 100%; 
            transition: all 0.2s ease;
        }

        .btn-submit:hover { 
            background: transparent;
            color: var(--text-primary);
        }

        h3 { 
            font-family: var(--font-mono);
            font-size: 13px; 
            text-transform: uppercase; 
            letter-spacing: 0.1em; 
            color: var(--text-muted);
            margin: 48px 0 16px 0;
            border-bottom: 1px solid var(--border);
            padding-bottom: 8px;
        }

        .file-list { 
            list-style-type: none; 
        }

        .file-item { 
            padding: 16px 0; 
            border-bottom: 1px solid var(--border); 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
        }

        .file-item:last-child {
            border-bottom: none;
        }

        .file-meta {
            display: flex;
            flex-direction: column;
            max-width: 60%;
        }

        .file-name { 
            font-size: 16px;
            color: var(--text-primary);
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .action-buttons {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .btn-download { 
            color: var(--text-primary); 
            text-decoration: none; 
            font-size: 13px; 
            font-weight: 700;
            text-transform: uppercase;
            font-family: var(--font-mono);
            border: 1px solid var(--border);
            padding: 8px 16px;
            transition: all 0.2s ease;
        }

        .btn-download:hover { 
            background: var(--text-primary);
            color: #000000;
            border-color: var(--text-primary);
        }

        .btn-delete {
            background: transparent;
            border: 1px solid transparent;
            cursor: pointer;
            padding: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-muted);
            transition: all 0.2s ease;
        }

        .btn-delete:hover {
            color: var(--danger);
            border-color: rgba(239, 68, 68, 0.2);
            background: rgba(239, 68, 68, 0.05);
        }

        .guide-box {
            margin-top: 48px;
            padding: 24px;
            background: #171717;
            border: 1px solid var(--border);
        }

        .guide-box h4 {
            margin-bottom: 16px;
            font-size: 13px;
            text-transform: uppercase;
            font-family: var(--font-mono);
            letter-spacing: 0.05em;
            color: var(--text-primary);
        }

        .guide-box ol {
            padding-left: 16px;
            font-size: 13px;
            color: var(--text-secondary);
            line-height: 1.7;
        }

        .guide-box li {
            margin-bottom: 12px;
        }

        .code-snippet {
            font-family: var(--font-mono);
            background: var(--bg);
            padding: 2px 6px;
            font-size: 12px;
            color: var(--success);
            border: 1px solid var(--border);
        }

        .github-link {
            display: inline-block;
            margin-top: 8px;
            font-size: 12px;
            font-family: var(--font-mono);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-primary);
            text-decoration: none;
            border-bottom: 1px dashed var(--text-secondary);
            padding-bottom: 2px;
            transition: all 0.2s ease;
        }
        
        .github-link:hover {
            border-bottom-color: var(--text-primary);
            color: var(--text-secondary);
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="badge">V1.0 // ACTIVE_NODE</div>
            <h1>LABSHARE</h1>
            <p class="subtitle">Upload file from One Device and download it to other within the same subnet(wifi)</p>
        </header>
        
        <form action="/upload" method="post" enctype="multipart/form-data">
            <div class="dropzone" onclick="document.getElementById('fileInput').click()">
                <span class="file-label" id="labelPlaceholder"> CHOOSE_FILE</span>
                <div class="file-chosen-name" id="fileNameDisplay">NULL</div>
                <input type="file" id="fileInput" name="file" required onchange="displayFileName(this)">
            </div>
            <button type="submit" class="btn-submit">Upload</button>
        </form>
        
        <h3>[UPLOADED_FILES]</h3>
        <ul class="file-list">
            {% if not files %}
                <li class="file-item" style="color: var(--text-muted); font-size: 13px; font-family: var(--font-mono); justify-content: center;">
                    // NO_OBJECTS_FOUND
                </li>
            {% endif %}
            {% for file in files %}
                <li class="file-item">
                    <div class="file-meta">
                        <span class="file-name" title="{{ file }}">{{ file }}</span>
                    </div>
                    <div class="action-buttons">
                        <a class="btn-download" href="/download/{{ file }}">Download</a>
                        <form action="/delete/{{ file }}" method="post" style="margin: 0;" onsubmit="return confirm('Confirm deletion of: {{ file }}?');">
                            <button type="submit" class="btn-delete" title="Delete object">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"></path><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6x"></path><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"></path></svg>
                            </button>
                        </form>
                    </div>
                </li>
            {% endfor %}
        </ul>

        <div class="guide-box">
            <h4>// HOW_TO_USE</h4>
            <ol>
                <li><strong>Push File:</strong> Trigger the select zone, isolate target document object, and execute <em>Publish</em> sequence.</li>
                <li><strong>Pull File:</strong> Engage the <em>Download</em> protocol to map files into target browser directory.</li>
                <li><strong>Deploy Layer:</strong> Clone repo -> install setup framework (<span class="code-snippet">pip install flask</span>) -> run application via terminal command <span class="code-snippet">python app.py</span>.</li>
            </ol>
            <a href="https://github.com/ah74n/labshare" target="_blank" class="github-link">
                [github_repo]
            </a>
        </div>
    </div>

    <script>
        function displayFileName(input) {
            const display = document.getElementById('fileNameDisplay');
            const placeholder = document.getElementById('labelPlaceholder');
            if (input.files && input.files.length > 0) {
                display.innerText = input.files[0].name.toUpperCase();
                placeholder.innerText = "CHOSEN_FILE_⬇️:";
                placeholder.style.color = "var(--success)";
            } else {
                display.innerText = "NULL";
                placeholder.innerText = "// SELECT_DOCUMENT";
                placeholder.style.color = "var(--text-primary)";
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML_TEMPLATE, files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)