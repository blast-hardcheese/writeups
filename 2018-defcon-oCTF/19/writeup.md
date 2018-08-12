"Do the needful" applies to this challenge quite well, as it's just a breadcrumb-style challenge with very clear next steps.

Step 1) Extract the file with `tar -xf DoTheNeedful-98e4c6ba71f88e4201a08e7503b0df6124607e39 Challenge.txt`
Step 2) Notice that the file looks very much like a base64 file, but reversed. Fortunately, `tac` (reverse `cat`) can fix this for us: `tac -r -s '.' < Challenge.txt > step2`
Step 3) Now that we have the base64 decoded, throw it through `base64`: `base64 -d < step2 > step3`
Step 4) `file` suggests that this file is a gzip. We know what to do with those: `gunzip < step3 > step4`
Step 5) This is somewhat of a jump, but the this is a sequence of hex characters evenly divisible by two. This could be a sequence of bytes that could be converted back to binary. Python makes quick work of this: `python -c "print ''.join([chr(int('466c61677b6577373332386866386573676839663233677d0a'[x*2:x*2+2], 16)) for x in xrange(0, 25)])"`

Answer: Flag{ew7328hf8esgh9f23g}

Bonus challenge: This can be rewritten as a one-liner:

`python -c "print ''.join([chr(int('$(tar -xOf DoTheNeedful-98e4c6ba71f88e4201a08e7503b0df6124607e39 Challenge.txt | tac -r -s '.' | base64 -d | gunzip)'[x*2:x*2+2], 16)) for x in xrange(0, 25)])"`
