gang_member = []
def add_member(name,age,gang):
    name_member = {
        'name': name,
        'age': age,
        'gang': gang,
    }
    gang_member.append(name_member)
    return name_member
while True:
    information_ask = input('ต้องการทำอะไร (1:เพิ่มสมาชิก) (2:ดูสมาชิกทั้งหมด) (Exit:ออกจากระบบ) : ')
    if information_ask == "1":
        name = (input("ชื่ออะไร : "))
        age = int(input("อายุเท่าไหร่ : "))
        gang = (input("อยู่แก๊งไหน : "))
        add_member(name,age,gang)
        print("เพิ่มข้อมูลเสร็จแล้ว")
    elif information_ask == "2":
        print(gang_member)
    else:
        print("ออกจากระบบเสร็จสิ้น")
    break