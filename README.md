# Network Logger and Visualizer

Ngambil status jaringan, di-output, terus di plot.

## Requirements

 - Perlu pakai linux.
 - Perlu ada command (beberapa sudah bawaan linux):
    - `sar`
    - `grep`
    - `tail`
    - `sed`
    - `tee`
 - Perlu library Python:
    - `pandas`
    - `matplotlib`

## How to Run

Jalankan 

```
./network-stat-log.py [Judul Plot]
```

atau

```
python network-stat-log.py [Judul Plot]
```

Hasil akan disimpan ke `output/[WAKTU]/`
