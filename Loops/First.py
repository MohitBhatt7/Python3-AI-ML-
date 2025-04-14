Diseases = ["Tuberculosis", "Cholera", "Typhoid_Fever", "Tetanus", "Measles", "Hepatitis"]
for disease in Diseases:
    print(disease)
for disease in Diseases:
    if disease == "Tuberculosis":
        for char in disease:
            print(char)
            
# Index for particular disease.

for i, disease in enumerate(Diseases):
    if disease == "Tuberculosis":
        print(f"The index for Tuberculosis in list is:- {i} .")
        
for disease in Diseases:
    if disease == Diseases[3]:
        break
    print(disease)
    
Vowels = "aeiouAEIOU"
for disease in Diseases:
    count = 0
    for char in disease:
        if char in Vowels:
            count += 1
            
        print(f"{disease} has {count} vowels ")