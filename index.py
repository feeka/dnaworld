
from flask import *
from forms import *
from algorithms.algorithms_01 import *
from algorithms.algorithms_03 import *
from algorithms.frequent_words_with_mismatches import *
from algorithms.minimum_skew import *
app = Flask(__name__)


ALGORITHMS=[
    {
        'name':'Reverse Complement',
        'input': 'A DNA string Pattern',
        'output': 'Pattern, the reverse complement of Pattern.',
        'route': 'revcompl',
        'info':'http://rosalind.info/problems/ba1c/'
    },
    {
        'name': 'Pattern Matching',
        'input': 'Pattern and Genome',
        'output' : 'A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome',
        'route':'patmatch',
        'info':'http://rosalind.info/problems/ba1d/'
    },
    {
        'name':'Pattern Count',
        'input': 'Strings Text and Pattern',
        'output': ' Count(Text, Pattern)',
        'route':'patcount',
        'info':'http://rosalind.info/problems/ba1a/'
    },
    {
        'name': 'Frequent Words',
        'input': 'A string Text and an integer k',
        'output' : 'All most frequent k-mers in Text',
        'route' : 'freqwords',
        'info' : 'http://rosalind.info/problems/ba1b/'
    },
    {
        'name':'Frequent Words with Mismatches',
        'input': 'A string Text as well as integers k and d',
        'output': 'All most frequent k-mers with up to d mismatches in Text',
        'route':'freqwordsmism',
        'info':'http://rosalind.info/problems/ba1i/'
    },
    {
        'name': 'Hamming Distance',
        'input': 'Two DNA strings',
        'output' : 'An integer value representing the Hamming distance',
        'route' : 'hammingdist',
        'info' : 'http://rosalind.info/problems/ba1g/'
    },
    {
        'name': 'Minimum Skew',
        'input': 'A DNA string Genome',
        'output' : 'All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|)',
        'route' : 'minskew',
        'info' : 'http://rosalind.info/problems/ba1f/'
    },
    {
        'name': 'Motif Enumeration',
        'input': 'Integers k and d, followed by a collection of strings Dna',
        'output' : 'All (k, d)-motifs in Dna',
        'route' : 'motifenum',
        'info' : 'http://rosalind.info/problems/ba2a/'
    },
    {
        'name': 'Median String',
        'input': 'An integer k, followed by a collection of strings Dna',
        'output' : 'A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers. (If there are multiple such strings Pattern, then you may return any one.)',
        'route' : 'medianstring',
        'info' : 'http://rosalind.info/problems/ba2b/'
    },
]

DATA_F = [
    {
        'name':'Introduction',
        'author': 'feeka',
        'date': '23.02.2020',
        'description': 'Here I would like to give an idea of why I decided to write little blogs.',
        'route': '../'
    },
    {
        'name':'DNA as a storage? Part 1.',
        'description': "The idea of possibility to consider DNA as a data storage medium is both exciting and risky. The idea has been around since 90's, however back then it seemed surreal just as touch screen mobile phone or any other innovation.",
        'author': 'feeka',
        'date' : '23.02.2020',
        'route': 'dnaasstorage'
    },
    {
        'name':'Domain specific language for bioinformatics?',
        'description':'The main idea in this post is to consider concepts of Model Driven Software Engineering as a potential to create DSL for bioinformaticians. Why is it useful?',
        'author':'feeka',
        'date':'24.02.2020',
        'route':'dslforbioinformatics'
    }
]
app.config['SECRET_KEY']="a286171ec581aac9872a89d13e6226a6"
@app.route('/')
def about():
    return render_template('about.html')

@app.route('/algorithms')
def hello_world():
    return render_template('index.html',algos=ALGORITHMS)
@app.route('/blog')
def blog():
    return render_template('blog.html',data=DATA_F)

@app.route('/blog/dnaasstorage')
def blog_dna_as_storage():
    return render_template('blog_dna_storage_one.html')

@app.route('/blog/dslforbioinformatics')
def blog_dsl_for_bio():
    return render_template('blog_mdse_dna.html')

@app.route('/home/freqwords', methods=('GET', 'POST'))
def freqwords():
    form = FreqWordsForm()
    if form.validate_on_submit():
        flash(f'Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        kval= int(form.k_val.data)
        result = FrequentWords(DNASeq,kval)
        return render_template('frequent_words.html',title="Frequent Words Algorithm", form=form, result=result)
    return render_template('frequent_words.html',title="Frequent Words Algorithm", form=form)

@app.route('/home/revcompl', methods=('GET', 'POST'))
def revcompl():
    form = ReverseComplementForm()
    if form.validate_on_submit():
        flash(f'Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        result = ReverseComplement(DNASeq)
        return render_template('reverse_complement.html',title="Reverse Complement Algorithm", form=form, result=result)
    return render_template('reverse_complement.html',title="Reverse Complement Algorithm", form=form)

@app.route('/home/patmatch', methods=('GET', 'POST'))
def patmatch():
    form = PatternMatchingForm()
    if form.validate_on_submit():
        flash(f'Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        pattern= form.pattern.data
        result = PatternMatching(pattern,DNASeq)
        return render_template('pattern_matching.html',title="Pattern Matching Problem", form=form, result=result)
    return render_template('pattern_matching.html',title="Pattern Matching Problem", form=form)

@app.route('/home/patcount', methods=('GET', 'POST'))
def patcount():
    form = PatternCountForm()
    if form.validate_on_submit():
        flash(f'Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        pattern= form.pattern.data
        result = PatternCount(DNASeq,pattern)
        return render_template('pattern_count.html',title="Pattern Count", form=form, result=result)
    return render_template('pattern_count.html',title="Pattern Count", form=form)

@app.route('/home/hammingdist', methods=('GET', 'POST'))
def hammingdist():
    form = HammingDistanceForm()
    if form.validate_on_submit():
        flash(f'Calculation successfully submitted','success')
        pattern_q = form.pattern_q.data
        pattern_p= form.pattern_p.data
        result = HammingDistance(pattern_q,pattern_p)
        return render_template('hamming_distance.html',title="Hamming Distance", form=form, result=result)
    return render_template('hamming_distance.html',title="Hamming Distance", form=form)

@app.route('/home/freqwordsmism', methods=('GET', 'POST'))
def freqwordsmism():
    form = FreqWordsWithMismatchForm()
    if form.validate_on_submit():
        flash(f'Calculation successfully submitted','success')
        dna_seq = form.dna_seq.data
        k_val= form.k_val.data
        distance=form.distance.data
        result = FrequentWordsWithMismatches(dna_seq,k_val,distance)
        print(result)
        return render_template('frequent_words_with_mismatches.html',title="Frequent words mismatches", form=form, result=result)
    return render_template('frequent_words_with_mismatches.html',title="Frequent words w/ mismatches", form=form)

@app.route('/home/minskew', methods=('GET', 'POST'))
def minskew():
    form = ReverseComplementForm()
    if form.validate_on_submit():
        flash(f'Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        result = MinimumSkew(DNASeq)
        return render_template('minimum_skew.html',title="Minimum Skew", form=form, result=result)
    return render_template('minimum_skew.html',title="Minimum Skew", form=form)


@app.route('/home/motifenum', methods=('GET', 'POST'))
def motifenum():
    form = FreqWordsWithMismatchForm()
    if form.validate_on_submit():
        flash(f'Calculation successfully submitted','success')
        dna_seq = form.dna_seq.data
        dna_update = dna_seq.split("\r\n")
        print(dna_update)
        k_val= form.k_val.data
        distance=form.distance.data
        result = motif_enumeration(dna_update,k_val,distance)
        print(result)
        return render_template('motif_enumeration.html',title="Motif Enumeration", form=form, result=result)
    return render_template('motif_enumeration.html',title="Motif Enumeration", form=form)

@app.route('/home/medianstring', methods=('GET', 'POST'))
def medianstring():
    form = FreqWordsForm()
    if form.validate_on_submit():
        flash(f'Calculation successfully submitted','success')
        dna_seq = form.dna_seq.data
        dna_update = dna_seq.split("\r\n")
        print(dna_update)
        k_val= int(form.k_val.data)
        result = MedianString(dna_update,k_val)
        print(result)
        return render_template('medianstring.html',title="Median String", form=form, result=result)
    return render_template('medianstring.html',title="Median String", form=form)




import os
port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)
