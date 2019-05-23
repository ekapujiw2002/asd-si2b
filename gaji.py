
def hitungGajiMingguan(jam_kerja_per_minggu=0.0):
    # 1. standar
    jamx = (0<jam_kerja_per_minggu<=48 and jam_kerja_per_minggu or
                           (jam_kerja_per_minggu>0 and 48 or 0)
                           )
    gaji_normal = 20000 * jamx
    jamy = (jam_kerja_per_minggu>48 and (jam_kerja_per_minggu-48.0) or 0)
    gaji_lembur = 25000 * jamy
    print("""
    Jam kerja total = %f
    Jam Kerja normal = %f
    Gaji Normal = %f
    Jam Kerja lembur = %f
    Gaji Lembur = %f
    """ %
          (jam_kerja_per_minggu,jamx,gaji_normal, jamy,gaji_lembur))
    
#hitungGajiMingguan()
#hitungGajiMingguan(20)
#hitungGajiMingguan(48)
#hitungGajiMingguan(50)
hitungGajiMingguan(55.6)