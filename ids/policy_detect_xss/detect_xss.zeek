@load base/protocols/http/main.zeek
@load base/protocols/http/utils.zeek
@load base/frameworks/notice
@load base/frameworks/sumstats
@load base/protocols/http
export {
    redef enum Notice::Type += {
        attack_xss,
    };
}

event tcp_packet(c: connection, is_orig: bool, flags: string, seq: count, ack: count, len: count, payload: string)
 {
 if ( is_orig && "<script>"  in payload || "</script>" in payload )
            {
            local n: Notice::Info = Notice::Info($note=attack_xss, 
                                                 $msg="attack xss ",
                                                 $sub=payload,
                                                 $conn=c);
            NOTICE(n);
            }

 }
