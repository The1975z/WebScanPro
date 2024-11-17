Cyber-Lab : WebScanPro
รายละเอียด Software:
WebScanPro เป็นเครื่องมือที่พัฒนาโดยใช้ภาษา Python สำหรับการประเมินความปลอดภัยของเว็บไซต์ เหมาะสำหรับนักทดสอบเจาะระบบ (Penetration Testers) และผู้เชี่ยวชาญด้านความปลอดภัยทางไซเบอร์ ตัวโปรแกรมสามารถสแกนเว็บไซต์เพื่อดึงข้อมูลสำคัญที่เกี่ยวข้อง เช่น พอร์ตที่เปิดอยู่ (Open Ports), ข้อมูล DNS, ข้อมูล WHOIS, รายละเอียดทางภูมิศาสตร์ (GeoIP), การตรวจสอบ Web Application Firewall (WAF) และช่องโหว่ที่อาจเกิดขึ้น เช่น การโจมตีด้วย SQL Injection
วัตถุประสงค์ :
วัตถุประสงค์ของ WebScanPro คือการช่วยให้ผู้เชี่ยวชาญด้านความปลอดภัยและผู้ดูแลระบบเครือข่ายสามารถตรวจสอบและวิเคราะห์ความปลอดภัยของเว็บแอปพลิเคชันล่วงหน้า การประเมินนี้ช่วยให้ทราบจุดที่เสี่ยงต่อการโจมตี เช่น พอร์ตที่อาจถูกเจาะ ช่องโหว่จากการตั้งค่าที่ไม่ปลอดภัย และปัญหาอื่นๆ เพื่อเพิ่มความปลอดภัยให้กับระบบ และยังสามารถเอาไปต่อยอดทําเป็น Tools ต่อได้ครับ
(Features) การทำงาน:
Open Port Scanning: สแกนพอร์ตที่พบได้บ่อย (1-1024) และแสดงพอร์ตที่เปิดพร้อมกับบริการที่เกี่ยวข้อง
DNS Information: ดึงข้อมูล DNS ของเป้าหมาย เช่น ชื่อโฮสต์ (Hostname), ที่อยู่ IP, และเซิร์ฟเวอร์ DNS
WHOIS Information: ดึงข้อมูล WHOIS ของ IP เป้าหมาย เช่น ผู้ลงทะเบียน (Registrar) และข้อมูลการเป็นเจ้าของ
GeoIP Information: รับข้อมูลทางภูมิศาสตร์ของเป้าหมาย เช่น เมือง, ภูมิภาค, ประเทศ และองค์กรที่ดูแล
Domain Registration Info: ข้อมูลการลงทะเบียนโดเมน เช่น ชื่อผู้ลงทะเบียนและประเทศที่จดทะเบียน
WAF Detection: ตรวจสอบว่าเว็บไซต์เป้าหมายมีการป้องกันโดย Web Application Firewall หรือไม่
SQL Injection Check: ตรวจสอบช่องโหว่ที่อาจเกิดขึ้นจาก SQL Injection ด้วย payload ที่ใช้บ่อย
Additional Server Info: ดึงข้อมูลเพิ่มเติมเกี่ยวกับเซิร์ฟเวอร์ เช่น วันที่สร้าง, ภาษาการเขียนโปรแกรม และข้อมูลเซิร์ฟเวอร์
## Requirements
- Python 3.x
- Python: `socket`, `requests`, `re`, `time`, `os`

## Installation
1. ดาวน์โหลดหรือโคลนโปรเจคจาก GitHub:
   ```bash
   git clone https://github.com/The1975z/WebScanPro.git
   ```
2. ไปยังไดเรกทอรีของโปรเจค:
   ```bash
   cd WebScanPro
   ```
3. ติดตั้งไลบรารีที่:
   ```bash
   pip install -r requirements.txt
   ```

## Features
- การสแกนพอร์ต
- ดึงข้อมูล DNS
- ข้อมูล WHOIS
- ตรวจสอบ GeoIP
- การตรวจสอบ WAF
- ทดสอบช่องโหว่ SQL Injection

## How to Use
1. รัน `python ToolsScanerWeb.py` ใน terminal
2. ป้อน URL ของเว็บไซต์ที่ต้องการสแกน
3. ดูข้อมูลที่แสดงบนหน้าจอ

## Functions
- `get_open_ports()`: สแกนพอร์ต
- `get_dns_info()`: ดึงข้อมูล DNS
- `get_whois_info()`: ดึงข้อมูล WHOIS
- `get_geoip_info()`: ตรวจสอบตำแหน่งทางภูมิศาสตร์
- `check_waf()`: ตรวจสอบ Web Application Firewall
- `check_sql_injection()`: ทดสอบช่องโหว่ SQL Injection
