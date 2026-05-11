# make sure to run this in the setup directory

mkdir -p ../inputs

rclone copy -P mnazareth:adig/adig_fatthin/nucleotide_diversity/out ../inputs

rclone copy mnazareth:adig/adig_fatthin/haplotype_phasing/out/AdiV3.2Ref_genome.fa.fai ../inputs

awk '{print $1, $2}' ../inputs/AdiV3.2Ref_genome.fa.fai > ../inputs/chrom.sizes

rclone copy -P mnazareth:adig/adig_fatthin/sliding_fst/out/fst_per_site.weir.fst ../inputs

rclone copy -P mnazareth:adig/adig_fatthin/sliding_fst/out/sliding_fst.windowed.weir.fst ../inputs