# CRA Payload Tool — Glossary

| Term | ความหมาย |
|---|---|
| CRA | Credit Risk Assessment |
| payload | JSON `{"inputs":[...]}` ที่ยิงเข้า scoring engine |
| Segment_ | MICRO, SME-LOWER, SME-M, SME-L, SME-UPPER1, SME-UPPER2 |
| ApplicationType_ | CA1 (quant ล้วน) หรือ CA2 (มี qualitative + 5C) |
| moduleId | โมดูล engine คำนวณจาก Segment + ApplicationType |
| 5C | Condition(6), Capital(5), Capacity(8), Character(7), Collateral(3) — เฉพาะ CA2 |

## Routing
| Segment_ | AppType | moduleId | 5C |
|---|---|---|---|
| MICRO | CA1 | ascore_ca1_v1 | ❌ |
| MICRO | CA2 | ascore_ca2_v1 | ✅ |
| SME-LOWER | CA2 | ascore_lower_ca2_v1 | ✅ |
| SME-UPPER1 | CA2 | ascore_upper1_ca2_v1 | ✅ |
| SME-M / SME-L / SME-UPPER2 | CA2 | ascore_upper2ml_v1 | ✅ |

URL = `https://productionengine.smebank.local/microanalyticScore/modules/{moduleId}/steps/execute`
