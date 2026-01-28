import math

class SaluranTerbuka:
    """
    Kelas untuk menangani perhitungan hidraulika saluran terbuka.
    Pemisahan ini memudahkan testing dan integrasi dengan AI.
    """
    
    @staticmethod
    def hitung_manning(b, h, s, n):
        """
        Menghitung kecepatan (V) dan debit (Q) menggunakan Rumus Manning.
        
        Parameter:
        b (float): Lebar dasar saluran (m)
        h (float): Tinggi muka air (m)
        s (float): Kemiringan dasar saluran (desimal, misal 0.001)
        n (float): Koefisien kekasaran Manning
        
        Returns:
        dict: Berisi hasil hitungan atau error message
        """
        try:
            # Validasi Input (Mencegah error matematika)
            if b <= 0 or h <= 0 or s <= 0 or n <= 0:
                return {"status": "error", "pesan": "Nilai parameter harus lebih besar dari 0"}

            # 1. Hitung Luas Penampang Basah (A) - Asumsi Persegi
            # (Nanti bisa dikembangkan untuk Trapesium)
            A = b * h
            
            # 2. Hitung Keliling Basah (P)
            P = b + (2 * h)
            
            # 3. Jari-jari Hidrolis (R)
            R = A / P
            
            # 4. Rumus Manning: V = (1/n) * R^(2/3) * S^(1/2)
            V = (1 / n) * (R ** (2/3)) * (s ** 0.5)
            
            # 5. Hitung Debit (Q)
            Q = V * A
            
            # 6. Angka Froude (Fr) - Cek aliran Kritis/Subkritis/Superkritis
            g = 9.81
            D = A / b # Kedalaman hidrolis (untuk persegi D = h)
            Fr = V / ((g * D)**0.5)
            
            aliran_type = "Subkritis (Tenang)" if Fr < 1 else "Superkritis (Cepat)"

            return {
                "status": "success",
                "V": round(V, 3),
                "Q": round(Q, 3),
                "Fr": round(Fr, 3),
                "Tipe_Aliran": aliran_type
            }

        except Exception as e:
            return {"status": "error", "pesan": str(e)}