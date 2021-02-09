import itertools
def proteins(strand):
    codon_aa_mapping = {   
                            'AUG' :	'Methionine',
                            'UUU' : 'Phenylalanine',
                            'UUC' : 'Phenylalanine',
                            'UUA' :	'Leucine',
                            'UUG' :	'Leucine',
                            'UCU' :	'Serine',
                            'UCC' :	'Serine',
                            'UCA' : 'Serine',
                            'UCG' :	'Serine',
                            'UAU' : 'Tyrosine',
                            'UAC' :	'Tyrosine',
                            'UGU' :	'Cysteine',
                            'UGC' : 'Cysteine',
                            'UGG' : 'Tryptophan'
                        }
    stop_codons = [ 'UAA', 'UAG', 'UGA']
    return [codon_aa_mapping[codon] for codon in itertools.takewhile(lambda c: c not in stop_codons, (strand[i:i+3] for i in range(0,len(strand), 3)))]
