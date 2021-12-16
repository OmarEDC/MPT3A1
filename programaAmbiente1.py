from faker import Faker #Importa biblioteca Faker

fake= Faker(['es_MX']) #Inicializa el generador de falsificaciones con el argumento de configuración regional de español México

print(fake.name())
print(fake.email())
print(fake.state())
print(fake.address())
print(fake.company())
print(fake.phone_number())
print(fake.ssn())

