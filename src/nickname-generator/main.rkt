#lang racket
(require web-server/servlet
         web-server/servlet-env)

(define names 
    (list
        'fred
        'goose
        'yoda
        'groot
        'water
        'violin
        'ball
        'grass
        'siesta
    ))

; returns a random name using names above
(define (get-random-name)
    (list-ref names (random (length names))))

(define (get-name-json-bytes)
    (string->bytes/utf-8 (format "{ \"name\": ~s }" (symbol->string (get-random-name)))))

(define (get-response)
    (response
        200 #"OK"
        (current-seconds) TEXT/HTML-MIME-TYPE
        empty
        (λ (op) (write-bytes (get-name-json-bytes) op))))

(define (start req)
    (get-response))

(serve/servlet start
    #:port 8081
    #:listen-ip "0.0.0.0"
    #:launch-browser? #f
    #:servlet-path "/")
