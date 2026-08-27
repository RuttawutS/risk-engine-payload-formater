# CRA Payload Tool — Glossary

| Term | ความหมาย |
|---|---|
| **CRA** | Credit Risk Assessment — การประเมินความเสี่ยงสินเชื่อของ SME Bank |
| **payload** | JSON `{"inputs":[...]}` ที่ยิงเข้า scoring engine (ฝั่ง REQUEST) |
| **Segment_** | ขนาด/กลุ่มลูกค้า: `MICRO`, `SME-LOWER`, `SME-M` (Medium), `SME-L` (Large), `SME-UPPER1`, `SME-UPPER2` |
| **ApplicationType_** | ประเภทคำขอ: `CA1` (quant ล้วน) หรือ `CA2` (มี qualitative + 5C) |
| **API2 / API6** | โหมดเรียก engine: API2 ↔ CA1, API6 ↔ CA2 (คำที่ใช้ในชื่อไฟล์ log) |
| **moduleId** | โมดูล engine ที่ประมวลผล คำนวณจาก Segment + ApplicationType |
| **5C** | คะแนน qualitative 5 มิติ: Condition(×6), Capital(×5), Capacity(×8), Character(×7), Collateral(×3) — มีเฉพาะ CA2 |
| **AF_Quantitative_** | ตารางงบการเงิน/ข้อมูลกิจการ 184 คอลัมน์ (1 metadata + 1 data row) ในฝั่ง REQUEST |
| **AF_Score** | ตารางผลคะแนนในฝั่ง RESPONSE |
| **RiskResult** | ผลสรุป: `Approve` / `Approve with condition` / `Reject` |
| **Risk color** | ระดับความเสี่ยงรายมิติ: Red > Orange > Yellow > Green |
| **A1 / A2 / Reject** | label ผลที่คาดหวังในชื่อไฟล์: A1=Approve, A2=Approve w/ condition, Reject |

## Routing (Segment + ApplicationType → moduleId)

| Segment_ | ApplicationType_ | moduleId | 5C |
|---|---|---|---|
| MICRO | CA1 | `ascore_ca1_v1` | ❌ |
| MICRO | CA2 | `ascore_ca2_v1` | ✅ |
| SME-LOWER | CA2 | `ascore_lower_ca2_v1` | ✅ |
| SME-UPPER1 | CA2 | `ascore_upper1_ca2_v1` | ✅ |
| SME-M / SME-L / SME-UPPER2 | CA2 | `ascore_upper2ml_v1` | ✅ |

URL = `https://productionengine.smebank.local/microanalyticScore/modules/{moduleId}/steps/execute`
