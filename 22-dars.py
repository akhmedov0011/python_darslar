def avto_info(kompaniya,model, **malumotlar):
    """avtomabillar haqidagi malumotlarni lugat ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar
print(avto_info("GM","lasetti",rangi="qora",yili=2018))