mkdir -p wig_files

python3 file_to_wig.py --input ./inputs/fst_per_site.weir.fst --type fst --output ./wig_files/adig_fatthin_fst.wig

python3 file_to_wig.py --input ./inputs/sliding_fst.windowed.weir.fst \
 --type window_fst --output ./wig_files/adig_fatthin_window_fst.wig \
 --window_step_size 10000

python3 file_to_wig.py --input ./inputs/digi_per_snp_pi.sites.pi \
 --type pi --output ./wig_files/digi_per_snp_pi.wig

python3 file_to_wig.py --input ./inputs/fat_digi_per_snp_pi.sites.pi \
 --type pi --output ./wig_files/fat_digi_per_snp_pi.wig

python3 file_to_wig.py --input ./inputs/digi_td_100bp_slide.windowed.pi \
 --type window_pi --output ./wig_files/digi_100bp_window_pi.wig \
 --window_step_size 100 

python3 file_to_wig.py --input ./inputs/fat_digi_td_100bp_slide.windowed.pi \
 --type window_pi --output ./wig_files/fat_digi_100bp_window_pi.wig \
 --window_step_size 100

python3 file_to_wig.py --input ./inputs/fat_digi_pi.Tajima.D \
 --type tajimas_d --output ./wig_files/fat_digi_tajimas_d_500bp_window.wig \
 --window_step_size 500

python3 file_to_wig.py --input ./inputs/digi_pi.Tajima.D \
 --type tajimas_d --output ./wig_files/digi_tajimas_d_500bp_window.wig \
 --window_step_size 500

