mkdir -p BigWig_files

eval "$(mamba shell hook --shell bash)"

mamba activate BigWig

WigToBigWig wig_files/adig_fatthin_fst.wig ./inputs/chrom.sizes BigWig_files/adig_fatthin_fst.bw
WigToBigWig wig_files/adig_fatthin_window_fst.wig ./inputs/chrom.sizes BigWig_files/adig_fatthin_window_fst.bw
WigToBigWig wig_files/digi_per_snp_pi.wig ./inputs/chrom.sizes BigWig_files/digi_per_snp_pi.bw
WigToBigWig wig_files/fat_digi_per_snp_pi.wig ./inputs/chrom.sizes BigWig_files/fat_digi_per_snp_pi.bw
WigToBigWig wig_files/digi_100bp_window_pi.wig ./inputs/chrom.sizes BigWig_files/digi_100bp_window_pi.bw
WigToBigWig wig_files/fat_digi_100bp_window_pi.wig ./inputs/chrom.sizes BigWig_files/fat_digi_100bp_window_pi.bw
WigToBigWig wig_files/fat_digi_tajimas_d_500bp_window.wig ./inputs/chrom.sizes BigWig_files/fat_digi_tajimas_d_100bp_window.bw
WigToBigWig wig_files/digi_tajimas_d_500bp_window.wig ./inputs/chrom.sizes BigWig_files/digi_tajimas_d_100bp_window.bw
