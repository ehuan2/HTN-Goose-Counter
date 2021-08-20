#lang racket
(require web-server/servlet
         web-server/servlet-env)

(define (get-response)
    (response
        301 #"OK"
        (current-seconds) TEXT/HTML-MIME-TYPE
        empty
        (λ (op) (write-bytes #"<html><body>Hello, World!</body></html>" op))))

(define (start req)
    (get-response))

(serve/servlet start
    #:port 8081
    #:listen-ip "0.0.0.0"
    #:launch-browser? #f
    #:servlet-path "/")
