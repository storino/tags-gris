section .data
    msg:    db 'Nao passou argumento', 0xa  ; message + newline

section .text
    global  _start

_start:
    cmp     qword [rsp], 2    ; confere se há argumento passado
    jne     falha             ; se não, pula para a rotina de falha
    mov     rax, 1            ; sys_write
    mov     rdi, 1            ; stdout
    mov     rsi, [rsp+16]     ; pega o endereço do argumento 
    mov     rdx, 1            ; comprimento 1

loop:
    cmp     byte [rsi], 0     ; confere se o char é 0
    je      exit              ; se 0, pula para terminar
    syscall
    inc     rsi               ; vai para o próximo char
    jmp     loop              ; loop

falha:
    mov     rax, 1            ; sys_write
    mov     rdi, 1            ; stdout
    lea     rsi, [rel msg]    ; movendo o endereço de msg para rsi
    mov     rdx, 21           ; comprimento de msg = 21
    syscall

exit:
    mov     rax, 60           ; sys_exit
    mov     rdi, 0            ; with code 0
    syscall
