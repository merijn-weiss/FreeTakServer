mkdir -p $HOME/.config/containers/systemd/
cp ./quadlets/* $HOME/.config/containers/systemd/
systemctl --user daemon-reload
systemctl --user restart freeTAKServer.service