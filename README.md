# CRA Payload Tool

Static web (ไฟล์ HTML เดียวจบ) สำหรับ CRA credit scoring payload ของ SME Bank

## ใช้งาน
เปิด **`cra_payload_tool.html`** ด้วย double-click (ไม่ต้อง server / build) มี 2 โหมด:

### 📖 อ่าน payload
วางได้ทั้ง: ไฟล์ `.log` เต็ม (มี `***REQUEST***` / `***RESPONSE***`), request JSON เดี่ยว, หรือ response JSON เดี่ยว
→ ระบบตรวจชนิดเอง แล้วแสดงเป็นหน้าอ่านง่าย: ข้อมูลลูกค้า, 5C, งบ AF_Quantitative (ย่อ+เต็ม), คะแนน, และสี risk 7 มิติ

### 🛠️ สร้าง payload
เลือก Segment + ApplicationType → tool คำนวณ moduleId + URL ให้ → กรอกฟิลด์สำคัญ (ที่เหลือใช้ default จาก payload จริง) → กด **สร้าง payload** → ได้ JSON ที่ยิงได้จริง 100% พร้อมปุ่มคัดลอก
- ค่าซ้ำ (ICR/DSCR/Installment/Term/Industry/ObjCode) **sync ลงทั้ง top-level และแถว AF อัตโนมัติ**
- CA1 = quant ล้วน (ไม่มี 5C) · CA2 = มี 5C

> หมายเหตุ: tool สร้าง JSON ให้คัดลอกไปยิงเอง (Postman/curl) — ไม่ยิง HTTP เองเพื่อเลี่ยง CORS/auth (ดู `docs/ADR.md`)

## โครงสร้าง
```
cra_payload_tool.html   ← ไฟล์ส่งมอบ (self-contained, ฝัง base template 7 แบบ)
_shell.html             ← source (มี placeholder ยังไม่ฝัง template)
docs/GLOSSARY.md        ← คำศัพท์ + ตาราง routing
docs/ADR.md             ← บันทึกการตัดสินใจออกแบบ
build/                  ← re-build ได้: python extract_templates.py && python build_tool.py
```

## Re-build (เมื่อแก้ _shell.html หรืออยากอัปเดต template จาก log)
```bash
cd cra_tool/build
python extract_templates.py   # ดึง template จาก log -> templates.json
python build_tool.py          # inject -> ../cra_payload_tool.html
```
