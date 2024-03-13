import streamlit as st
import random

class Rrrandomnumber:
    def __init__(self, time=1):
        self.time = time

    def timex():
        Rrrandomnumber.time = st.number_input("จำนวนครั้งที่สุ่ม", value=1)

    @staticmethod
    def randomx(numbermin, numbermax):
        if isinstance(numbermin, int) and isinstance(numbermax, int):
            if numbermin <= numbermax:
                r = random.randint(numbermin, numbermax)
                st.title(r) 
            else:
                st.title("ตัวเลขของคุณไม่ถูกต้อง")
        else:
            st.title("ไม่ใช่ตัวเลข")

class Rrrandomlanguage(Rrrandomnumber):
    thai = ["ก","ข","ฃ","ค","ฅ","ฆ","ง","จ","ฉ","ช","ซ","ฌ","ญ","ฎ","ฏ","ฐ","ฑ","ฒ","ณ","ด","ต","ถ","ท","ธ","น","บ","ป","ผ","ฝ","พ","ฟ","ภ","ม","ย","ร","ฤ","ล","ฦ","ว","ศ","ษ","ส","ห","ฬ","อ","ฮ"]
    loas = ["ຄ","ງ","ຈ","ສ","ຊ","ຍ","ດ","ຕ","ຖ","ທ","ນ","ບ","ປ","ຜ","ຝ","ພ","ຟ","ມ","ຢ","ຣ","ລ","ວ","ສ","ຫ","ອ","ຮ"]
    English = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    B = ["นกบก","นกกระจอก","นกกระเต็น","นกกระเรียน","นกกระสา","นกกวาง","นกขุนทอง","นกจุด","นกเขาใหญ่","นกเค้าจอก","นกเงือก","นกจาบคาง","นกจิ้งจก","นกฉัตร","นกชวา","นกชัดเขา","นกชัดลม","นกชั้น","นกชัย","นกชายเลน","นกซอก","นกซีดา","นกซีเรียง","นกดาบ","นกดำ","นกต่อ","นกตั๊กแตน","นกถั่ง","นกทับทิม","นกทับทิมพันธ์","นกทาบาห์","นกทาหาด","นกทาเรียน","นกทาห่อง","นกทาเรียนบ้าน","นกทิพย์","นกนกเขา","นกน้อย","นกน้ำดัด","นกบก","นกบดินทร์","นกบาบี","นกปล่อยขี้","นกปล่อยนก","นกปลาดาว","นกปลาหมอ","นกปลาแม่","นกปักกิ่ง","นกปากเกร็ด","นกปากช่อน","นกปากแดง","นกปากหมาก","นกปู่เจ้า","นกผึ้ง","นกพิราบ","นกพิราม","นกฟ้า","นกฟ้าฮูก","นกฟ้าหงอน","นกฟ้าร้อง","นกฟ้าลม","นกฟ้าเล็ก","นกมงคล","นกมนุษย์","นกมวย","นกมังกร","นกมังคี","นกมังคุด","นกมังคุดปลายหาง","นกมังคุดหน้าแดง","นกมังคุดหัวเหล็ก","นกมังคุดหางขาว","นกมังคุดโคก","นกมัน","นกม้า","นกยูง","นกลาย","นกลายจุด","นกลายทอง","นกลายผึ้ง","นกลายยักษ์","นกลายหงอน","นกลายเสือ","นกลายแพะ","นกลายไพร","นกลายไร่","นกลายไอ","นกลุง","นกลุงป่า","นกวงเวียน","นกวาง","นกว่าว","นกว่าน","นกสั้น","นกสาปสัตว์","นกสาว","นกสิงโต","นกสีเขียว","นกสีเรียน","นกสีแดง","นกสุนัข","นกสุพรรณ","นกสุริยา","นกสุริยาอินทร์","นกสุริยาวรรณ","นกสุริยเด่น","นกหงส์","นกหวด","นกหอย","นกหอยปู","นกหัตถ์","นกหางหมู","นกหางสนวน","นกหางเล็ก","นกหางเหลือง","นกหางแดง","นกหางแหลม","นกหางแร้ว","นกหางสั้น","นกหางสิบ","นกหางสามเหลี่ยม","นกหางหนาม","นกหางหยั่ง","นกหางห่าน","นกหางหาย","นกหางอ่อน","นกหางเหล"]

    def __init__(self, time=1):
        super().__init__(time)

    @staticmethod
    def randomx(language):
        if isinstance(language, str):
            if language == "thai":
                r = random.choice(Rrrandomlanguage.thai)
                st.title(r)  
            elif language == "loas":
                r = random.choice(Rrrandomlanguage.loas)
                st.title(r) 
            elif language == "English":
                r = random.choice(Rrrandomlanguage.English)
                st.title(r) 
            elif language == "สัตว์ปีก":
                r = random.choice(Rrrandomlanguage.B)
                st.title(r)
            else:
                st.title("ไม่รองรับภาษานี้")
        else:
            st.title("ไม่รองรับภาษานี้")

class Rrrandomx(Rrrandomlanguage):
    def __init__(self, time=1):
        super().__init__(time)

    @staticmethod
    def randomx(txt):
        if isinstance(txt, str):
            items = txt.split(",")
            r = random.choice(items)
            st.write(r)
        else:
            st.write("ไม่สามารถสุ่มได้")

# สร้างเว็บแอป Streamlit
def main():
    st.title("rrRandom")
    st.write("")
    st.write("")
    st.write("")
    
    option = st.selectbox(
        "เลือกประเภท:",
        ("Random ตัวเลข", "Random เเบบหมวดหมู่","Random เเบบเพิ่มเอง")
    )

    if option == "Random ตัวเลข":
        min_value = st.number_input("ค่าเริ่มต้น", value=0)  
        max_value = st.number_input("ค่าสุดท้าย", value=99)
        Rrrandomnumber.timex()
        if st.button("สุ่มม!!!"):
            for u in range(Rrrandomnumber.time):
                Rrrandomnumber.randomx(min_value, max_value)

    elif option == "Random เเบบหมวดหมู่":
        optionlanguage = st.selectbox("เลือกภาษา:",("thai", "loas","English","สัตว์ปีก"))
        Rrrandomnumber.timex()
        if st.button("สุ่มม!!!"):
            for u in range(Rrrandomnumber.time):
                if optionlanguage == "English":
                    Rrrandomlanguage.randomx("English")
                if optionlanguage == "thai":
                    Rrrandomlanguage.randomx("thai")
                if optionlanguage == "loas":
                    Rrrandomlanguage.randomx("loas")
                if optionlanguage == "สัตว์ปีก":
                    Rrrandomlanguage.randomx("สัตว์ปีก")
  

    elif option == "Random เเบบเพิ่มเอง":
        txt = st.text_area("เพิ่มสิ่งที่ต้องการสุ่ม คั่นด้วย ','")
        Rrrandomnumber.timex()
        if st.button("สุ่มม!!!"):
            Rrrandomx.randomx(txt)

if __name__ == "__main__":
    main()


