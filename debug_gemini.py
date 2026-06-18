from app.services.ai_service import analyze_prescription

result = analyze_prescription("""
                              Paracetamol 650mg
                              Take twice daily after food
                              Drink plenty of water
                              """)

print(result)