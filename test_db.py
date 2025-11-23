import psycopg2

# Ganti 'your_password' dengan password PostgreSQL Anda
try:
    conn = psycopg2.connect(
        host="localhost",
        database="de_learning",
        user="postgres",
        password="juniormahfud"  # Password Anda
    )

    print("[SUCCESS] Connected to PostgreSQL successfully!")

    # Test query
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"\nPostgreSQL version: {version[0][:80]}...")

    cursor.close()
    conn.close()
    print("\n[SUCCESS] Connection closed properly!")
    print("\n" + "="*50)
    print("All tests passed! PostgreSQL & Python works!")
    print("="*50)

except psycopg2.OperationalError as e:
    print(f"[ERROR] Cannot connect to PostgreSQL: {e}")
    print("\nPossible fixes:")
    print("1. Check PostgreSQL service is running")
    print("2. Verify password is correct")
    print("3. Make sure database 'de_learning' exists")
    
except Exception as e:
    print(f"[ERROR] Unexpected error: {e}")