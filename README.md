# CRA Payload Tool

Static web (HTML ไฟล์เดียว) สำหรับ CRA credit-scoring payload ของ SME Bank
2 โหมด: **อ่าน payload** ให้เข้าใจง่าย และ **สร้าง payload** ที่ยิงได้จริงจากฟอร์ม + ปุ่มคัดลอก

## เปิดใช้
เปิด `index.html` ด้วยเบราว์เซอร์ (double-click) — ไม่ต้อง build/server

## Deploy บน GitHub Pages
1. push โฟลเดอร์นี้ขึ้น repo
2. Settings → Pages → Source = **Deploy from a branch** → `main` / root (`/`)
   (หรือใช้ GitHub Actions workflow ใน `.github/workflows/deploy-pages.yml` ที่ให้มา)
3. เปิด URL ที่ Pages แจ้ง เช่น `https://<org-or-user>.github.io/<repo>/`

> ⚠️ **ข้อมูล**: `index.html` ในโฟลเดอร์นี้เป็น **dummy-data** (ค่าเริ่มต้นว่าง/ศูนย์) จึงปลอดภัยแม้ repo/Pages เป็นสาธารณะ
> เวอร์ชันที่ฝัง payload ตัวอย่างจริง (`cra_payload_tool_INTERNAL.html`) **ห้ามขึ้น public** — ใช้ภายใน/GitHub Enterprise เท่านั้น

## โครงสร้าง
```
index.html      ← ตัวเครื่องมือ (dummy-data, self-contained)
_shell.html     ← source (มี placeholder ยังไม่ฝัง template)
docs/           ← GLOSSARY.md, ADR.md
.github/workflows/deploy-pages.yml  ← auto-deploy Pages
```
