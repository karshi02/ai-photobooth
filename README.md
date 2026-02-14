# 📸 AI Photobooth – System Design & Principles

AI Photobooth คือระบบถ่ายภาพอัตโนมัติที่สามารถ
- ถ่ายรูปผู้ใช้
- รักษา “หน้าเดิม คนเดิม”
- เปลี่ยนชุด / ธีม / สถานที่ / ฉาก
- ได้ภาพใหม่แบบสมจริง โดยไม่ต้องบันทึกรูปต้นฉบับถาวร

เอกสารนี้อธิบาย **หลักการทำงานของระบบทั้งหมด** ตั้งแต่ระดับแนวคิด → AI → Implementation

---

## 1. ภาพรวมแนวคิด (Concept)

AI Photobooth **ไม่ใช่ Face Swap**

แต่คือ:
> “การสร้างภาพใหม่ โดยใช้ตัวตน (Identity) ของคนเดิมเป็นเงื่อนไข”

สิ่งที่เปลี่ยน:
- เสื้อผ้า
- ฉาก
- สไตล์
- บรรยากาศ

สิ่งที่ต้องเหมือนเดิม:
- หน้า
- โครงหน้า
- ลักษณะบุคคล

---

## 2. Flow การทำงานของระบบ

[ กล้อง ]
↓
[ รูปคน ]
↓
[ แยกตัวตน (Identity) ]
↓
[ เลือกธีม / ชุด / ฉาก ]
↓
[ AI Generate ภาพใหม่ ]
↓
[ แสดงผล / พิมพ์ ]


**ไม่มีการ Save รูปต้นฉบับถาวร**  
ใช้เฉพาะใน Memory ระหว่างการประมวลผล

---

## 3. AI หลักที่ใช้ในระบบ

ระบบ AI Photobooth ประกอบด้วย 3 ส่วนสำคัญ

### 3.1 Face & Identity Extraction
ใช้เพื่อ “จำหน้าคน”

หน้าที่:
- ดึงลักษณะเฉพาะของหน้า (facial embedding)
- เก็บเป็นตัวแทน (Identity Vector)

ผลลัพธ์:
- ไม่ใช่รูป
- เป็นข้อมูลเชิงตัวเลขแทนหน้า

---

### 3.2 Image Generation (Text-to-Image)

AI สร้างภาพจาก:
- Prompt (ข้อความ)
- Identity (ตัวตนของคน)

ตัวอย่าง Prompt:
A realistic photo of the same person,
wearing a samurai armor,
cinematic lighting,
high detail


---

### 3.3 Identity Conditioning (หัวใจของระบบ)

จุดนี้คือสิ่งที่ทำให้:
> หน้าเดิม คนเดิม แต่ชุดเปลี่ยน

AI จะถูกบังคับด้วย:
- ตัวตน (face embedding)
- โครงหน้า
- สัดส่วน

ไม่ใช่การแปะหน้า (Face Swap)

---

## 4. ทำไมไม่ใช้ Face Swap

| Face Swap | AI Photobooth |
|---------|--------------|
| เอาหน้าไปแปะ | สร้างภาพใหม่ทั้งใบ |
| มักดูหลอก | ดูสมจริง |
| แสงไม่เข้ากัน | แสงถูกต้อง |
| หน้าแข็ง | หน้าเป็นธรรมชาติ |

Photobooth ที่ดี **ต้องไม่รู้สึกว่าโดนตัดต่อ**

---

## 5. โครงสร้างระบบ (Demo Version)

ai-photobooth/
│
├─ app/
│ ├─ main.py # ตัวควบคุมระบบ
│ ├─ config.py # ตั้งค่า
│ │
│ ├─ ai/
│ │ ├─ pipeline.py # AI generation pipeline
│ │ └─ prompts.py # Prompt แต่ละธีม
│ │
│ ├─ input/
│ │ └─ person.jpg # รูปจากกล้อง (ชั่วคราว)
│ │
│ ├─ output/
│ │ └─ result.png # ภาพที่ได้
│ │
│ └─ ui/
│ └─ demo_ui.py # UI demo
│
├─ requirements.txt
└─ README.md


---

## 6. หลักการ “ไม่บันทึกรูป”

ระบบจะ:
1. รับภาพจากกล้อง
2. Extract identity
3. Generate ภาพใหม่
4. ลบภาพต้นฉบับจาก memory

✔ ปลอดภัย  
✔ เหมาะกับพื้นที่สาธารณะ  
✔ ไม่มีข้อมูลตกค้าง

---

## 7. ประเภท AI Model ที่ใช้

### ระดับ Demo (PC)
- Text-to-Image Diffusion
- CPU / GPU

### ระดับใช้งานจริง (ตู้)
- Identity-conditioned Diffusion
- GPU แยก
- Queue งานแบบ Real-time

---

## 8. ข้อจำกัดที่ต้องรู้

- เครื่องไม่มี GPU → ช้า
- Identity lock คุณภาพสูง → ต้องใช้ model เฉพาะ
- ยิ่ง real-time → ยิ่งกินพลังประมวลผล

---

## 9. Roadmap การพัฒนา

- [x] โครงสร้างระบบ
- [x] Prompt-based generation
- [ ] Identity lock
- [ ] UI เลือกธีม
- [ ] กล้อง + จอสัมผัส
- [ ] ระบบพิมพ์ภาพ
- [ ] ระบบลบข้อมูลอัตโนมัติ

---

## 10. สรุปสั้น ๆ

AI Photobooth =  
> การสร้างภาพใหม่  
> โดยเอา “ตัวตนของคน”  
> ไปใส่ใน “โลกใหม่”

ไม่ใช่แต่งรูป  
ไม่ใช่ Face Swap  
แต่คือ **Generative AI เต็มรูปแบบ**

---