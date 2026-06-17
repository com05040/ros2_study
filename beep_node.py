import sys
import subprocess


def main():
    ns = 'robot9'

    for arg in sys.argv:
        if arg.startswith('namespace:='):
            ns = arg.split(':=')[1]

    cmd = f'''timeout 5s ros2 topic pub -r 1 /{ns}/cmd_audio irobot_create_msgs/msg/AudioNoteVector "{{append: false, notes: [
      {{frequency: 880.0, max_runtime: {{sec: 0, nanosec: 300000000}}}},
      {{frequency: 440.0, max_runtime: {{sec: 0, nanosec: 300000000}}}},
      {{frequency: 880.0, max_runtime: {{sec: 0, nanosec: 300000000}}}},
      {{frequency: 440.0, max_runtime: {{sec: 0, nanosec: 300000000}}}}
    ]}}"'''

    subprocess.run(cmd, shell=True)


if __name__ == '__main__':
    main()