# -*- coding: utf-8 -*-
import os
import re

html_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    c = f.read()

issues = []

# 1. 152-FZ Check
if 'type="checkbox"' not in c or '152-ФЗ' not in c:
    issues.append("152-FZ notice missing")
if 'id="quiz-consent" checked' in c:
    issues.append("Quiz consent is checked by default!")
if 'id="modal-consent" checked' in c:
    issues.append("Modal consent is checked by default!")

# 2. Target blank
for m in re.finditer(r'<a\s+[^>]*target=["\']_blank["\'][^>]*>', c, re.IGNORECASE):
    tag = m.group(0)
    if 'rel=' not in tag or 'noopener' not in tag:
        issues.append(f"target=_blank without rel=noopener: {tag}")

# 3. Instagram / Facebook ban
if re.search(r'instagram\.com|facebook\.com', c, re.IGNORECASE):
    issues.append("Unmarked forbidden social network found")

# 4. Check image files existence
for m in re.finditer(r'src=["\']([^"\']+\.jpg)["\']', c):
    src = m.group(1)
    if not src.startswith("http"):
        local_path = os.path.join(os.path.dirname(html_path), src.replace("/", os.sep))
        if not os.path.exists(local_path):
            issues.append(f"Image not found: {src} -> {local_path}")

# 5. Check emojis
emojis = [ch for ch in c if ord(ch) > 0x10000]
if emojis:
    issues.append(f"Emojis found: {set(emojis)}")

print("=== VERIFICATION REPORT ===")
if issues:
    for i in issues:
        print("  ❌ ISSUE:", i)
    exit(1)
else:
    print("  ✅ 100% QUALITY GATE PASSED: ZERO ISSUES DETECTED!")
