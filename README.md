# Test Platform

Bu dastur Excel fayllardan test savollarini import qilish va test o'tkazish uchun mo'ljallangan.

## Imkoniyatlar

- Excel fayllardan test savollarini import qilish
- Test savollarini ko'rsatish va javoblarni qabul qilish
- Javoblarni tekshirish va natijalarni ko'rsatish
- Test natijalarini ko'rish

## Excel fayl formati

Excel fayl quyidagi formatda bo'lishi kerak:
- A ustun: Test raqami
- B ustun: Savol matni
- C, D, E, F ustunlar: Javob variantlari
- G ustun: To'g'ri javobning to'liq matni (C, D, E yoki F ustunlaridan birida ko'rsatilgan javob matni bilan 100% mos kelishi kerak)

**Muhim**: Savollar 2-qatordan boshlanishi kerak!

## O'rnatish

Dasturni ishga tushirish uchun quyidagi dependencylarni o'rnatish kerak:

```
pip install -r requirements.txt
```

## Dasturni ishga tushirish

```
python test_app.py
```

## Ishlatish bo'yicha qo'llanma

1. Dastur ishga tushganda "Import Excel File" tugmasini bosing
2. Excel faylni tanlang
3. Savollarga javob bering
4. "Check Answer" tugmasini bosib javobingizni tekshiring
5. "Next" tugmasi orqali keyingi savolga o'ting
6. Test yakunida "Finish Test" tugmasini bosib natijalarni ko'ring
#   t e s t _ a p p  
 