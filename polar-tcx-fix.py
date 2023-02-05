import re
from os import path, listdir

in_dir = "/home/chris/Downloads/in"
out_dir = "/home/chris/Downloads/out"

unchanged = 0
changed = 0
multi = 0

unformatted_patch = "<BuildMajor>0</BuildMajor><BuildMinor>0</BuildMinor>"

formatted_patch = (
    "  <BuildMajor>0</BuildMajor>\n        <BuildMinor>0</BuildMinor>\n      "
)

for filename in [f for f in listdir(in_dir) if f.lower().endswith(".tcx")]:
    with open(path.join(in_dir, filename), "r", encoding="utf-8") as file:
        data = file.read()

        res, cnt = re.subn(
            r"(<Author .*>.*<Build>\s+<Version>.*</VersionMinor>\s+)"
            + r"(</Version>\s+</Build>.*</Author>)",
            r"\1  <BuildMajor>0</BuildMajor>\n"
            + r"        <BuildMinor>0</BuildMinor>\n      \2",
            data,
            count=1,
            flags=re.DOTALL,
        )
        if cnt == 0:
            res, cnt = re.subn(
                r"(<Author .*>.*<Build><Version>.*</VersionMinor>)"
                + r"(</Version></Build>.*</Author>)",
                r"\1<BuildMajor>0</BuildMajor><BuildMinor>0</BuildMinor>\2",
                data,
                count=1,
                flags=re.DOTALL,
            )

        with open(path.join(out_dir, filename), "w", encoding="utf-8") as out:
            out.write(res)

        print(f"{cnt} times replaced in {filename}")

        if cnt <= 0:
            unchanged += 1
        else:
            changed += 1
        if cnt > 1:
            multi += 1

print(
    f"Processed {unchanged + changed} files, {changed} updated, {unchanged}"
    f"unchanged. Unecpected multi changes: {multi}"
)
