# Architecture Decision Records — CRA Payload Tool

## ADR-001 — เครื่องมือสร้าง JSON ให้ก็อป ไม่ยิง HTTP เอง
**Decision:** หน้าเว็บ generate payload ที่ถูกต้อง 100% แล้วให้ผู้ใช้ copy ไปยิงเองผ่าน Postman/curl
**Why:** static page ยิงตรงไป `productionengine.smebank.local` จะติด CORS / auth / เข้าถึง network ภายในไม่ได้ การแยก "สร้าง" ออกจาก "ยิง" ทำให้เครื่องมือทำงานได้ทุกที่และไม่มี dependency
**Consequence:** ต้องแสดง endpoint URL ให้ด้วย เพื่อให้ผู้ใช้รู้ว่ายิงไปไหน

## ADR-002 — Base template จาก payload จริง (capture-and-overlay)
**Decision:** ดึง REQUEST payload จริงจาก log ตัวอย่าง 7 แบบมาเป็น base template ฝังในไฟล์ ฟอร์มแค่ overlay ฟิลด์สำคัญทับ
**Why:** AF_Quantitative มี 184 คอลัมน์ที่ต้องถูกต้องจึงจะยิงได้จริง การให้กรอกครบเป็นไปไม่ได้ การ clone payload จริงแล้วแก้เฉพาะจุด รับประกันโครงสร้างถูกเสมอ
**Consequence:** payload ที่สร้างจะอิงข้อมูล default ของเคสตัวอย่าง (คอลัมน์ที่ไม่ได้แก้) — เหมาะกับ test/QA ไม่ใช่ข้อมูล production จริงรายคน

## ADR-003 — Sync ค่าซ้ำอัตโนมัติ (single source of truth)
**Decision:** ฟิลด์ที่ปรากฏทั้ง top-level และในแถว AF_Quantitative (Installment, TermYear, ICR, DSCR, ObjCodeDetail, IndustryType, IncomePerYear, Limit) กรอกครั้งเดียว เขียนลงทั้งสองที่
**Why:** กันค่าขัดกันจน engine ให้ผลเพี้ยน เขียนโดย map ตามชื่อคอลัมน์ (ไม่ hardcode index) จึงทนต่อการเปลี่ยนลำดับ
**Consequence:** ฟอร์มถือเป็นเจ้าของค่าเดียว ผู้ใช้ไม่ต้องรู้ว่ามันซ้ำกันอยู่

## ADR-004 — Driver คือ Segment_ + ApplicationType_ ไม่ใช่ token CA1/CA2 ในชื่อไฟล์
**Decision:** routing และการมี 5C อิง Segment_ + ApplicationType_ ในตัว payload เท่านั้น
**Why:** พบว่า token CA1/CA2 ในชื่อไฟล์ไม่ตรงกับ ApplicationType_ จริง (ไฟล์ SME ชื่อ CA1 แต่ payload เป็น CA2 ทั้งหมด) มีแค่ MICRO เท่านั้นที่เป็น CA1 จริง
**Consequence:** UI จำกัด ApplicationType ตาม Segment (MICRO เลือก CA1/CA2 ได้, SME เป็น CA2 เท่านั้น)

## ADR-005 — Reader รับ input ได้หลายรูปแบบ auto-detect
**Decision:** ช่องอ่านรับได้ทั้งไฟล์ .log เต็ม (มี marker), request JSON เดี่ยว, หรือ response JSON เดี่ยว โดยตรวจชนิดเอง
**Why:** ยืดหยุ่นสุด ตรงเป้าหมาย "อ่านง่าย" ผู้ใช้ไม่ต้องแยกส่วนเอง

## ADR-006 — จัดการ AF_Score ที่คอลัมน์เพี้ยนของ module ca2
**Decision:** ถ้าจำนวนค่าใน data row ≠ จำนวน metadata columns ให้แสดง warning + ค่าดิบตามตำแหน่ง
**Why:** module `ascore_ca2_v1` (Micro CA2) คืน AF_Score ที่ค่าสีเกินมา 1 ตำแหน่งหน้าสุด zip ตรงๆ จะ map ผิด
