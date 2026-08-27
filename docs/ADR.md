# ADR — CRA Payload Tool

- **ADR-001** สร้าง JSON ให้ก็อป ไม่ยิง HTTP เอง (เลี่ยง CORS/auth)
- **ADR-002** base template จาก payload จริง (capture-and-overlay) การันตี AF 184 คอลัมน์ถูก
- **ADR-003** sync ค่าซ้ำ (ICR/DSCR/Installment/Term/Industry/ObjCode) ลงทั้ง top-level และ AF โดย map ตามชื่อคอลัมน์
- **ADR-004** routing ยึด Segment_ + ApplicationType_ (token CA1/CA2 ในชื่อไฟล์เชื่อไม่ได้)
- **ADR-005** reader auto-detect: รับ .log เต็ม / request / response
- **ADR-006** เตือนเมื่อ AF_Score ของ ascore_ca2_v1 คอลัมน์เพี้ยน
- **ADR-007 (deploy)** repo/Pages สาธารณะใช้ index.html แบบ dummy-data เท่านั้น; เวอร์ชันข้อมูลจริง (INTERNAL) ใช้ภายใน/Enterprise เท่านั้น
