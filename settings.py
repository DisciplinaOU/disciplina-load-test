# faucet test settings
FAUCET_BASE_URL = 'https://faucet.disciplina.io/api/faucet/v1/'
FAUCET_CREATE_WALLET_URL = FAUCET_BASE_URL + 'keygen'
FAUCET_TRANSFER_URL = FAUCET_BASE_URL + 'transfer'

# explorer test settings
EXPLORER_BASE_URL = 'https://witness.disciplina.io/api/witness/v1/'
EXPLORER_ACCOUNT_INFO = EXPLORER_BASE_URL + 'accounts/'
EXPLORER_BLOCKS = EXPLORER_BASE_URL + 'blocks/'
EXPLORER_TRANSACTIONS = EXPLORER_BASE_URL + 'transactions/'

# student test settings
STUDENT_BASE_URL = 'http://localhost:8090/api/student/v1/'
STUDENT_COURSES = STUDENT_BASE_URL + 'courses/'
STUDENT_ASSIGNMENTS = STUDENT_BASE_URL + 'assignments/'
STUDENT_SUBMISSIONS = STUDENT_BASE_URL + 'submissions/'
STUDENT_PROOFS = STUDENT_BASE_URL + 'proofs/'
