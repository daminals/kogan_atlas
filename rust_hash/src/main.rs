use hex_literal::hex;
use sha2::{Sha256, Sha512, Digest};

fn main() {
    // create a Sha256 object
    let mut hasher = Sha256::new();

    // write input message
    hasher.update(b"hello world");

    // read hash digest and consume hasher
    let result = hasher.finalize();

    assert_eq!(result[..], hex!("
        b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
    ")[..]);

    // same for Sha512
    let mut hasher = Sha512::new();
    hasher.update(b"hello world");
    let result = hasher.finalize();
    println!("{:?}", result);

    assert_eq!(result[..], hex!("
        309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f
        989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f
    ")[..]);
}