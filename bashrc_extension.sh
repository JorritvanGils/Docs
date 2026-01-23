setup_ssh_agent() {
    export SSH_AUTH_SOCK=$(ls /tmp/ssh-*/agent.* 2>/dev/null | head -n1)
    [ -z "$SSH_AUTH_SOCK" ] && SSH_AUTH_SOCK=/tmp/ssh-agent.sock

    if ! ssh-add -l >/dev/null 2>&1; then
        rm -f "$SSH_AUTH_SOCK" 2>/dev/null
        eval "$(ssh-agent -s -a /tmp/ssh-agent.sock)" >/dev/null 2>&1
        export SSH_AUTH_SOCK=/tmp/ssh-agent.sock
    else
        if [ -f "$HOME/.ssh/kingkey" ]; then
            local kingkey_fingerprint
            kingkey_fingerprint=$(ssh-keygen -lf "$HOME/.ssh/kingkey" 2>/dev/null | awk '{print $2}')
            if [ -n "$kingkey_fingerprint" ]; then
                ssh-add -l | grep -q "$kingkey_fingerprint" && ssh-add -d "$HOME/.ssh/kingkey" >/dev/null 2>&1
            fi
        fi
    fi
}

add_ssh_key_silently() {
    local key_file="$1"
    local pass_var="$2"

    [ ! -f "$key_file" ] && { echo "Key file not found: $key_file"; return 1; }
    
    /usr/bin/expect <<EOF >/dev/null 2>&1 # -t 32400 = 9 hours
        set timeout 5
        spawn ssh-add -t 32400 "$key_file"
        expect "Enter passphrase" { send "${!pass_var}\r" }
        expect eof
EOF
    local result=$?
    [ $result -ne 0 ] && echo "Failed to add key $key_file (exit code $result)" >&2
    return $result
}

setup_ssh_agent
command -v expect >/dev/null || echo "Warning: 'expect' not found. Did you install it?"
add_ssh_key_silently "$HOME/.ssh/farmkey" "FARM_PW" &
add_ssh_key_silently "$HOME/.ssh/queenkey" "QUEEN_PW" &

wait

# ssh-add -l



CACHE_DIR="$HOME/.cache/bittensor"
mkdir -p "$CACHE_DIR"
CACHE_FILE="$CACHE_DIR/last_update_check"

auto_update_system() { # 7 × 24 × 60 × 60
    if [ -f "$CACHE_FILE" ] && [ $(date +%s) -lt $(( $(cat "$CACHE_FILE") + 604800 )) ]; then
        return
    fi

    echo "🛠️  Running system"

    sudo apt update && sudo apt upgrade -y

    date +%s > "$CACHE_FILE"
}

auto_update_system


alias S="source ~/.bashrc"
alias B="nano +9999 ~/.bashrc"
alias N="python /media/jorrit/ssd/bittensor/remote_gpu/navigator.py"
alias 38="python /media/jorrit/ssd/bittensor/remote_gpu/navigator.py 38"
alias 3="python /media/jorrit/ssd/bittensor/remote_gpu/navigator.py 3"
alias J='read -p "Docker action: [1] status, [2] start, [3] stop? " c; if [[ $c == 1 ]]; then sudo systemctl status docker; elif [[ $c == 2 ]]; then sudo systemctl start docker; elif [[ $c == 3 ]]; then sudo systemctl stop docker.socket docker.service; else echo "Invalid choice"; fi'
# alias V='source /media/jorrit/ssd/career/test_project/.venv/bin/activate'

Z() {
    grep -E '^alias (S|B|N|J)=' "/media/jorrit/ssd/bittensor/remote_gpu/bashrc_extension.sh"
}