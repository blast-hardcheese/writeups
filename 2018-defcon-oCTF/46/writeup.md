This is an automated breadcrumb challenge. Fortunately largely regularly structured, but initially unknown data formats.

First, evaluating what we're even dealing with, we open a socket connection to the host:
nc 172.31.2.59 51966

    ACM: Talk to the machine
    decode each of these formats as fast as possible!
    if you properly solve each of the 12 challenges, you get the flag!
    c3RyaW5ne2pwMnFoY0ZZRjBLYlZFQ1Y5ZjVLZWlibXBnUnAwaHRXfQ==

    ?

This is actually two packets: The first is the game prompt, the second is the first challenge. This looks like base64.

Decoding and submitting that gives us morse code:

    .-- .. ..- --- -.- -- .- ..-. .... --- --.. -.-- -.-- --. .-.. -- .--- .-- -... .-.. .-- --.- ..- .- --- -... --- ... ..- ... ..-. .--.

    ?

doing the same with the morse code gives us another challenge:

    01110011011101000111001001101001011011100110011101111011011000100110101000110100010011100011100100110001001110010101000001100011001101000100001001101010010101000110000101111000010100110101001101111010010010110110111101100001010100100101001101101101001101110110100000110001011011110011010101010100011000100100000101111101 

    ?

and another...

    73 74 72 69 6e 67 7b 69 66 6f 5a 75 4a 55 57 74 7a 67 42 6e 4a 65 50 4a 4d 47 79 61 37 70 42 74 65 57 53 6f 37 54 4a 7d

    ?

Fortunately, it seems as though these are the only formats represented in the game.

The only challenge now is the detection logic. The "binary" format is a subset of base64, so we just need to make sure we try binary before base64:

    answer = morse(res) or binary(res) or chars(res) or b64(res) or unknown(res)

After many tries, we eventually get:

Answer: OpenCTF{Good_job_on_being_faster_than_a_human!}
