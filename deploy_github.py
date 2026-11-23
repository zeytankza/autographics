# -*- coding: utf-8 -*-
"""
GitHub Repository Creation and GitHub Pages Deployment Script
for Auto Graphics (Pyatigorsk)
"""

import subprocess
import urllib.request
import json
import os
import sys

def get_token():
    p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, _ = p.communicate(input='protocol=https\nhost=github.com\n\n')
    for line in stdout.splitlines():
        if line.startswith('password='):
            return line.split('=', 1)[1]
    return None

def create_or_get_repo(token, repo_name="autographics"):
    url = "https://api.github.com/user/repos"
    payload = json.dumps({
        "name": repo_name,
        "description": "Официальный сайт детейлинг-центра «Авто Графикс» (Пятигорск) — Оклейка полиуретаном PPF, автовинил, защита кузова",
        "private": False,
        "has_pages": True
    }).encode("utf-8")
    
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"token {token}",
        "User-Agent": "AutoGraphicsDeployer",
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.v3+json"
    })
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"✅ Репозиторий '{repo_name}' успешно создан на GitHub: {data.get('html_url')}")
            return data
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        if e.code == 422 and "already exists" in err_body:
            print(f"ℹ️ Репозиторий '{repo_name}' уже существует на GitHub.")
            return {"html_url": f"https://github.com/zeytankza/{repo_name}"}
        else:
            print(f"❌ Ошибка создания репозитория ({e.code}): {err_body}")
            sys.exit(1)

def push_to_github(repo_name="autographics"):
    cwd = os.path.dirname(os.path.abspath(__file__))
    remote_url = f"https://github.com/zeytankza/{repo_name}.git"
    
    # Check if remote exists
    remotes = subprocess.run(["git", "remote"], cwd=cwd, capture_output=True, text=True).stdout
    if "origin" in remotes.split():
        subprocess.run(["git", "remote", "set-url", "origin", remote_url], cwd=cwd, check=True)
    else:
        subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=cwd, check=True)
    
    print(f"📡 Remote 'origin' установлен на: {remote_url}")
    print("🚀 Выполняю push в ветку main...")
    push_res = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=cwd, capture_output=True, text=True)
    if push_res.returncode == 0:
        print("✅ Успешно запушено в GitHub!")
        print(push_res.stdout)
    else:
        print("❌ Ошибка при push:")
        print(push_res.stderr)
        sys.exit(1)

def enable_pages(token, repo_name="autographics"):
    url = f"https://api.github.com/repos/zeytankza/{repo_name}/pages"
    payload = json.dumps({
        "source": {
            "branch": "main",
            "path": "/"
        }
    }).encode("utf-8")
    
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"token {token}",
        "User-Agent": "AutoGraphicsDeployer",
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.v3+json"
    })
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            pages_url = data.get("html_url", f"https://zeytankza.github.io/{repo_name}/")
            print(f"✅ GitHub Pages успешно активирован: {pages_url}")
            return pages_url
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        if e.code == 409 or "already has a Pages site" in err_body:
            pages_url = f"https://zeytankza.github.io/{repo_name}/"
            print(f"ℹ️ GitHub Pages уже был активирован ранее: {pages_url}")
            return pages_url
        else:
            print(f"⚠️ Ответ при включении Pages ({e.code}): {err_body}")
            pages_url = f"https://zeytankza.github.io/{repo_name}/"
            return pages_url

def main():
    token = get_token()
    if not token:
        print("❌ Не удалось получить токен GitHub из credential helper.")
        sys.exit(1)
    
    create_or_get_repo(token, "autographics")
    push_to_github("autographics")
    pages_url = enable_pages(token, "autographics")
    print(f"\n🎉 Все готово! Публичная ссылка: {pages_url}")

if __name__ == "__main__":
    main()
