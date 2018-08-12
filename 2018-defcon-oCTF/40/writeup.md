"Firewalker" is a term for walking through firewalls.

We are given two URLs:
- One including the term flag
- Another suggesting the firewall rules that are in place

The rules are in a non-compressed tarball, and are as follows:

    Chain PORT_20621 (1 references)
    target     prot opt source               destination         
    REJECT     tcp  --  anywhere             anywhere             tcp spts:1024:65535 reject-with icmp-admin-prohibited

We can see all high _source_ ports are rejected.

Fortunately, netcat permits controlling the source port:

    echo 'GET /flag-d12bb978.txt' | sudo nc -p 1000 172.31.2.97 20621

Answer: pr1vil3ge_h4s_its_privile9e5
